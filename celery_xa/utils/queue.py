try:
    import thread
except ImportError:
    import dummy_thread as thread
    
class Queue(object):
    store = {}

    def _has_list(self):
        thread_ident = thread.get_ident()
        return thread_ident in self.store
        
    def _init_list(self):
        thread_ident = thread.get_ident()
        assert thread_ident not in self.store
        self.store[thread_ident] = []
        return self.store[thread_ident]
        
    def _remove_list(self):
        thread_ident = thread.get_ident()
        assert thread_ident in self.store
        del self.store[thread_ident]
    
    def _get_list(self):
        thread_ident = thread.get_ident()
        assert thread_ident in self.store
        return self.store[thread_ident]
        
    def _get_or_init_list(self):
        if self._has_list():
            return self._get_list()
        else:
            return self._init_list()        
    
    @property
    def queue(self):
        return self._get_or_init_list()
    
    def clear(self):
        self._remove_list()
    
store = Queue()