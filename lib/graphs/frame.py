import vaex
from pyarrow.parquet import read_table

import lib.fs as fs

class Frame(object):
    def __init__(self, pqfile):
        self.df = vaex.from_arrow_table(read_table(pqfile))
        self.name = fs.basename(pqfile)[:-8] #-4: remove '.parquet'
        self.benign = self.name.endswith('b')

    def get_nice_name(self):
        return self.name[:-2] #-2 to remove '_b' or '_m'

    def is_benign_set(self):
        return self.benign

    def get_amount(self):
        return len(self.df)

    def get_exec_time_total(self):
        return self.df.sum(self.df.totaltime)

    def get_exec_time_average(self):
        return self.get_exec_time_total() / len(self.df)

    def get_had_succes_total(self):
        return self.df.length(selection=(not self.df.error) and (not self.df.timout))


    def get_had_timeout_total(self):
        return self.df.length(selection=self.df.timeout)

    def get_lines_timeout(self):
        return self.df[df.timeout]


    def get_had_error_total(self):
        return self.df.length(selection=self.df.error)

    def get_lines_error(self):
        return self.df[df.error]


    def get_html_total_size(self):
        return self.df.sum(self.df.htmlsize)

    def get_html_average_size(self):
        return self.get_html_total_size() / len(self.df)


    def get_problems_total(self):
        return self.df.length(selection=self.df.timeout or self.df.error)

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if not isinstance(other, Frame):
            return NotImplemented
        return self.name == other.name and self.is_benign_set() == other.is_benign_set()

    def __lt__(self, other):
        if not isinstance(other, Frame):
            return NotImplemented
        
        if self.name == other.name:
            return self.is_benign_set
        return self.name < other.name

    def __hash__(self):
        return hash(str(self))

    def __len__(self):
        return len(self.df)