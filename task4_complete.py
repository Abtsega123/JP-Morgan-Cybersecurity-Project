class RolesCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.roles = {}
        self._lru = {}
        self._tick = 0

    def get(self, role):
        if role in self.roles:
            self._lru[role] = self._tick
            self._tick += 1
            return self.roles[role]
        return -1

    def set(self, role, message):
        if role not in self.roles and len(self.roles) >= self.capacity:
            cur_oldest_role = None
            cur_oldest_tick = float('inf')
            roles = self.roles.keys()
            for r in roles:
                if self._lru[r] < cur_oldest_tick:
                    cur_oldest_role = r
                    cur_oldest_tick = self._lru[r]
            self.roles.pop(cur_oldest_role)
            self._lru.pop(cur_oldest_role)
        self.roles[role] = message
        self._lru[role] = self._tick
        self._tick += 1

    def _complexity(self):
        return {
            'get': 'O(1)',
            'set': 'O(N)', # optimal solution is O(1)
            'space': 'O(N)'
        }