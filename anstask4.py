
class RolesCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.roles = {}
        self.queue = []

    def get(self, role):
        if role in self.roles:
            return self.roles[role]
        else:
            return None

    def set(self, role, message):
        if role in self.roles:
            self.roles[role] = message
        else:
            if len(self.queue) == self.capacity:
                oldest_role = self.queue.pop(0)
                del self.roles[oldest_role]
            self.roles[role] = message
            self.queue.append(role)

    def _complexity(self):
        return {
            'get': 'O(1)',
            'set': 'O(1)',
            'space': 'O(k)'
        }
