import lib.fs as fs
from lib.graphs.csv.dataline import Dataline

class CSV(object):
    def __init__(self, csvfile):
        self.lines = []
        self.name = fs.basename(csvfile)[:-4] #-4: remove '.csv'
        self.benign = self.name.endswith('b')
        self.from_file(csvfile)
        self.lines.sort()

    def get_nice_name(self):
        return self.name[:-2] #-2 to remove '_b' or '_m'

    def is_benign_set(self):
        return self.benign

    def get_amount(self):
        return len(self.lines)

    def get_exec_time_total(self):
        return sum([x.total_time for x in self.lines])

    def get_exec_time_average(self):
        return self.get_exec_time_total() / len(self.lines)

    def get_had_succes_total(self):
        return len([x for x in self.lines if (not x.errors) and (not x.timout)])


    def get_had_timeout_total(self):
        return len(self.get_lines_timeout())

    def get_lines_timeout(self):
        return [x for x in self.lines if x.timout]


    def get_had_error_total(self):
        return len(self.get_lines_error())

    def get_lines_error(self):
        return [x for x in self.lines if x.errors]


    def get_html_total_size(self):
        return sum([x.html_size for x in self.lines])

    def get_html_average_size(self):
        return self.get_html_total_size() / len(self.lines)

    def get_parsed_ok_total(self):
        return len([x for x in self.lines if (not x.timout) and (not x.errors)])

    def get_problems_total(self):
        return len([x for x in self.lines if x.timout or x.errors])

    def from_file(self, csvfile):
        with open(csvfile, 'r') as csv:
            self.lines.extend([Dataline.init_from_line(x) for x in csv])

    # def generator_parsed_ok(self):
    #     for x in self.lines:
    #         if (not x.timeout) and (not x.errors):
    #             yield x

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if not isinstance(other, CSV):
            return NotImplemented
        return self.name == other.name and self.is_benign_set() == other.is_benign_set()

    def __lt__(self, other):
        if not isinstance(other, CSV):
            return NotImplemented
        
        if self.name == other.name:
            return self.is_benign_set
        return self.name < other.name

    def __hash__(self):
        return hash(str(self))

    def __len__(self):
        return len(self.lines)