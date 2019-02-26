class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, start, end):
        if len(self.events) == 0:
            self.events.append([start, end])

            return True

        return self._add_event(start, end)

    def _add_event(self, start, end):
        low = 0
        high = len(self.events) - 1

        insert_index = self._find_event_intersection(low, high, start)

        # figure out if new event should be added before or after intersection
        if start > self.events[insert_index][0]:
            insert_index += 1

        print(insert_index)

        if self._is_intersect(insert_index, start, end):
            return False

        if insert_index < len(self.events):
            self.events.insert(insert_index, [start, end])
        else:
            self.events.append([start, end])

        return True

    def _find_event_intersection(self, low, high, start):
        if high <= low:
            return low

        mid = low + int((high - low) / 2)
        if self.events[mid][0] < start:
            # search upper half
            return self._find_event_intersection(mid + 1, high, start)

        elif self.events[mid][0] > start:
            # search lower half
            return self._find_event_intersection(low, mid - 1, start)
        else:
            return mid

    def _is_intersect(self, intersect_index, start, end):
        if intersect_index < len(self.events) and intersect_index >= 0:
            next_event = self.events[intersect_index]
            if end > next_event[0]:
                return True

        if intersect_index - 1 >= 0:
            prev_event = self.events[intersect_index - 1]
            if start < prev_event[1]:
                return True

        return False