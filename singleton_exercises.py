import datetime
import threading


class NumberGenerator:
    _instance = None
    _lock = threading.Lock()
    _current_number = 0

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def get_next_number(self):
        with self._lock:
            number = self._current_number
            self._current_number += 1
        return number


# def test_singleton_thread_safe():
#     ng = NumberGenerator()
#     print(f'Generated number: {ng.get_next_number()}')
#
#
# threads = []
# for i in range(100):
#     thread = threading.Thread(target=test_singleton_thread_safe)
#     threads.append(thread)
#     thread.start()
#
#
# for t in threads:
#     t.join()


class FileAuditManager:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, file_name='audit.log'):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._file_name = file_name
                with open(cls._instance._file_name, 'a') as file:
                    file.write(f'Log started: {datetime.datetime.now()}\n')
        return cls._instance

    def log_message(self, message):
        with self._lock:
            with open(self._instance._file_name, 'a') as file:
                file.write(f'{datetime.datetime.now()}: {message}\n')


def test_singleton_thread_safe():
    logger = FileAuditManager('test_audit.log')
    logger.log_message('Test message from thread')


threads = []
for i in range(100):
    thread = threading.Thread(target=test_singleton_thread_safe)
    threads.append(thread)
    thread.start()


for t in threads:
    t.join()
