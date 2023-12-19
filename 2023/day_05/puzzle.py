from utils.debugging import PrintDebug


class ConversionMap:
    def __init__(self, name, debug_context):
        self.debug = debug_context
        self.name = name
        # input is array of arrays:  [dest range start, source range start, range length]
        self.conversion_codes = []
        # but map is easier-to-use array [ source range start, source range end, offset ]
        self.map = []

    def set_conversion_codes(self, conversion_codes):
        self.conversion_codes = conversion_codes
        self.setup_map(self.conversion_codes)

    def setup_map(self, conversion_codes):
        self.debug.increase_indent()
        self.debug.print(2, f"setting up map {self.name}")
        self.debug.increase_indent()
        self.debug.print(2, f"with conversion codes {conversion_codes}")
        for dest_range_start, source_range_start, range_length in conversion_codes:
            if range_length > 0:
                source_range_end = source_range_start + range_length
                offset = dest_range_start - source_range_start
                self.map.append([source_range_start, source_range_end, offset])
        self.debug.print(2, f"resulting in maps: {self.map}")
        self.debug.decrease_indent()
        self.debug.decrease_indent()

    def map_value(self, value):
        mapping = [x for x in self.map if x[0] <= value <= x[1]]
        if mapping:
            self.debug.print(3, f"{self.name} mapping value {value} to {value + mapping[0][2]}")
            return value + mapping[0][2]
        else:
            self.debug.print(3, f"{self.name} mapping value {value} to {value}")
            return value

    def map_intervals(self, intervals):
        new_interval_list = []
        self.debug.increase_indent()
        self.debug.print(3, f"{self.name} mapping ranges {intervals}")
        self.debug.increase_indent()
        self.debug.print(3, f"using maps {self.map}")
        while len(intervals) > 0:
            interval = intervals.pop()
            self.debug.increase_indent()
            self.debug.print(7, f"checking maps for {interval}, using {interval[0]}")
            # self.debug.print(7, f"x[0] values for maps are {[x[0] for x in self.map]}")
            # self.debug.print(7, f"x[1] values for maps are {[x[1] for x in self.map]}")
            mapping = [x for x in self.map if max(interval[0], x[0]) <= min(interval[1], x[1])]
            if mapping:
                self.debug.increase_indent()
                self.debug.print(7, f"found map for interval {interval}: {mapping}")
                self.debug.decrease_indent()
                offset = mapping[0][2]
                self.debug.increase_indent()
                if interval[0] <= mapping[0][0]:
                    if interval[1] <= mapping[0][1]:  # case: interval overlaps on left side of map
                        self.debug.print(6, f"interval {interval} overlaps map {mapping[0][0]}, {mapping[0][1]} on left side")
                        self.debug.increase_indent()
                        self.debug.print(6, f"splitting into [{interval[0]}, {mapping[0][0] -1}], [{mapping[0][0]}, {interval[1]}:+ {offset}]")
                        self.debug.decrease_indent()
                        if interval[0] < mapping[0][0]:
                            intervals.append((interval[0], mapping[0][0] - 1))  # could match another map
                        new_interval_list.append((mapping[0][0] + offset, interval[1] + offset))
                    else:  # case: map entirely contained in interval
                        self.debug.print(6, f"interval {interval} entirely contains map {mapping[0][0]}, {mapping[0][1]}")
                        self.debug.increase_indent()
                        self.debug.print(6, f"splitting into [{interval[0]}, {mapping[0][0] -1}], [{mapping[0][0]}, {mapping[0][1]}: +{offset}], and [{mapping[0][1] +1}, {interval[1]}]")
                        self.debug.decrease_indent()
                        if interval[0] < mapping[0][0]:
                            intervals.append((interval[0], mapping[0][0] - 1))  # could match another map
                        if interval[1] > mapping[0][1]:
                            intervals.append((mapping[0][1] + 1, interval[1]))  # could match another map
                        new_interval_list.append((mapping[0][0] + offset, mapping[0][1] + offset))
                else:
                    if interval[1] <= mapping[0][1]:  # case: interval entirely contained in map
                        self.debug.print(6, f"interval {interval} entirely contained by map {mapping[0][0]}, {mapping[0][1]}")
                        self.debug.increase_indent()
                        self.debug.print(6, f"returning [{interval[0]}, {interval[1]}: + {offset}]")
                        self.debug.decrease_indent()
                        new_interval_list.append((interval[0] + offset, interval[1] + offset))
                    else:   # case: interval overlaps right side of map
                        self.debug.print(6, f"interval {interval} overlaps map {mapping[0][0]}, {mapping[0][1]} on right side")
                        self.debug.increase_indent()
                        self.debug.print(6, f"splitting into [{interval[0]}, {mapping[0][1]}: + {offset}], [{mapping[0][1] +1 }, {interval[1]}]")
                        self.debug.decrease_indent()
                        intervals.append((mapping[0][1] + 1, interval[1]))
                        new_interval_list.append((interval[0] + offset, mapping[0][1] + offset))
                self.debug.decrease_indent()
            else:
                self.debug.print(6, f"no map found for interval {interval}")
                self.debug.increase_indent()
                self.debug.print(6, f"passing [{interval[0]}, {interval[1]}] unchanged")
                self.debug.decrease_indent()
                new_interval_list.append(interval)
            self.debug.decrease_indent()
        self.debug.print(3, f"{self.name} returning ranges {new_interval_list}")
        self.debug.decrease_indent()
        self.debug.decrease_indent()
        return new_interval_list


class Puzzle:
    fileName: str

    def __init__(self, file_name, puzzle_part, debug_level):
        self.fileName = file_name
        self.puzzle_part = puzzle_part
        self.debug = PrintDebug(debug_level)
        self.debug_level = debug_level
        self.seeds = []
        self.seed_to_soil_map = ConversionMap("seed to soil", self.debug)
        self.soil_to_fertilizer_map = ConversionMap("soil to fertilizer", self.debug)
        self.fertilizer_to_water_map = ConversionMap("fertilizer to water", self.debug)
        self.water_to_light_map = ConversionMap("water to light", self.debug)
        self.light_to_temperature_map = ConversionMap("light to temperature", self.debug)
        self.temperature_to_humidity_map = ConversionMap("temp to humid", self.debug)
        self.humidity_to_location_map = ConversionMap("humid to loc", self.debug)
        self.lowest_location = -1
        self.initial_seed_intervals = []
        self.final_seed_intervals = []

    def print_run_info(self):
        self.debug.print(1, f"{chr(10)}PUZZLE RUN:  running part {self.puzzle_part} with file "
                            f"{self.fileName} and debug level {self.debug_level}")

    def print(self):
        pass

    @staticmethod
    def parse_blank_line_terminated_records(lines):
        record = []
        for line in lines:
            if line.strip():
                record.append(line)
            elif record:
                yield record
                record = []
        if record:
            yield record

    def parse(self):
        with open(self.fileName) as file:
            current_map = self.soil_to_fertilizer_map
            for rec in self.parse_blank_line_terminated_records(file):
                mappings = []
                for line in rec:
                    if line.startswith('seeds:'):
                        seed_line = line.split(':')
                        self.seeds = [int(x) for x in seed_line[1].split()]
                        self.debug.increase_indent()
                        self.debug.print(2, f"found seeds: {self.seeds}")
                        self.debug.decrease_indent()
                    elif line.startswith('seed-to-soil'):
                        current_map = self.seed_to_soil_map
                    elif line.startswith('soil-to-fertilizer'):
                        current_map = self.soil_to_fertilizer_map
                    elif line.startswith('fertilizer-to-water'):
                        current_map = self.fertilizer_to_water_map
                    elif line.startswith('water-to-light'):
                        current_map = self.water_to_light_map
                    elif line.startswith('light-to-temperature'):
                        current_map = self.light_to_temperature_map
                    elif line.startswith('temperature-to-humidity'):
                        current_map = self.temperature_to_humidity_map
                    elif line.startswith('humidity-to-location'):
                        current_map = self.humidity_to_location_map
                    else:
                        mappings.append([int(x) for x in line.split()])
                if mappings:
                    current_map.set_conversion_codes(mappings)

    def chunker(self, seq, size):
        return (seq[pos:pos + size] for pos in range(0, len(seq), size))

    def get_seeds(self):
        if self.puzzle_part == "a":
            self.debug.print(2, f"returning {self.seeds}")
            for seed in self.seeds:
                yield seed
        else:
            for group in self.chunker(self.seeds, 2):
                self.debug.print(2, f"found chunk {group}")
                for seed in range(group[0], group[0] + group[1]):
                    self.debug.print(2, f"yielding seed: {seed}")
                    yield seed

    def find_lowest_location(self):
        for i in self.get_seeds():
            self.debug.print(2, f"checking location for seed {i}")
            self.debug.increase_indent()
            tmp_location = self.humidity_to_location_map.map_value(
                self.temperature_to_humidity_map.map_value(
                    self.light_to_temperature_map.map_value(self.water_to_light_map.map_value(
                        self.fertilizer_to_water_map.map_value(
                            self.soil_to_fertilizer_map.map_value(self.seed_to_soil_map.map_value(i)))))))
            self.debug.increase_indent()
            self.debug.print(3, f"location for seed {i} is {tmp_location}")
            self.debug.decrease_indent()
            self.debug.decrease_indent()
            if self.lowest_location == -1:
                self.lowest_location = tmp_location
            elif tmp_location < self.lowest_location:
                self.lowest_location = tmp_location
        return self.lowest_location

    def solve(self):
        self.print_run_info()
        self.parse()
        self.print()
        if self.puzzle_part == "a":
            for i in self.seeds:
                self.debug.print(1, f"seed {i} maps to {self.seed_to_soil_map.map_value(i)}")
            return self.find_lowest_location()
        else:
            self.calculate_initial_seed_intervals()
            self.calculate_final_seed_intervals()
            return min([x[0] for x in self.final_seed_intervals])
