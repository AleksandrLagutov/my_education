import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    def append(self, el):
        super(LoggableList, self).append(el)
        return self.log(el)

a = LoggableList()
a.append('msg 1')
a.append('msg 2')
print(a)