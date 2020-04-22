class Dataline(object):
    """Data object for dataline"""
    def __init__(self,tool_name,html_name,html_size,total_time,links_found,
        ru_utime,ru_stime,ru_maxrss,ru_minflt,ru_majflt,errors,timeout):
        self.tool_name = tool_name
        self.html_name = html_name
        self.html_size = int(html_size)
        self.total_time = float(total_time)
        self.links_found = int(links_found)
        self.ru_utime = float(ru_utime)
        self.ru_stime = float(ru_stime)
        self.ru_maxrss = int(ru_maxrss)
        self.ru_minflt = int(ru_minflt)
        self.ru_majflt = int(ru_majflt)
        self.errors = errors == 'True'
        self.timeout = timeout == 'True'

    @staticmethod
    def init_from_line(line):
        return Dataline(*(line.rstrip().split(',')))

    # def anonymize(self):
    #     return Dataline('',self.apk_name,self.is_malware,self.exec_time,
    #         self.had_warnings,self.had_succes,self.had_timeout,
    #         self.apk_size,self.malicious)

    def __str__(self):
        return '{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11}'.format(
            self.tool_name,
            self.html_name,
            self.html_size,
            self.total_time,
            self.links_found,
            self.ru_utime,
            self.ru_stime,
            self.ru_maxrss,
            self.ru_minflt,
            self.ru_majflt,
            self.errors,
            self.timeout)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if not isinstance(other, Dataline):
            return NotImplemented
        return str(self) == str(other)

    def __lt__(self, other):
        if not isinstance(other, Dataline):
            return NotImplemented
        return self.html_name < other.html_name

    def __hash__(self):
        return hash(str(self))
