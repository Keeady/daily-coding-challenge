class MyCalendar:

    def __init__(self):
        self.events = [[8, 10], [10, 20], [20, 30], [35, 45]]

    def book(self, start, end):
        if len(self.events) == 0:
            self.events.append([start, end])

            return True

        return self._add_event(start, end)

    def _add_event(self, start, end):
        low = 0
        high = len(self.events) - 1

        [intersect_index_low, intersect_index_high] = self._find_event_intersection(low, high, start)

        is_intersect_low = self._is_intersect(intersect_index_low, start, end)
        is_intersect_high = self._is_intersect(intersect_index_high, start, end)

        if is_intersect_low or is_intersect_high:
            return False

        # figure out if new event should be added before or after intersection
        insert_index = intersect_index_low

        if start < self.events[intersect_index_high][0]:
            if start > self.events[intersect_index_low][0]:
                insert_index = intersect_index_low + 1
        else:
            insert_index = intersect_index_high + 1

        if insert_index < len(self.events):
            self.events.insert(insert_index, [start, end])
        else:
            self.events.append([start, end])

        return True

    def _find_event_intersection(self, low, high, start):
        if high - low <= 1:
            return [low, high]

        mid = low + int((high - low) / 2)
        if self.events[mid][0] < start:
            # search upper half
            return self._find_event_intersection(mid, high, start)

        elif self.events[mid][0] > start:
            # search lower half
            return self._find_event_intersection(low, mid, start)
        else:
            return [mid, mid]

    def _is_intersect(self, intersect_index, start, end):
        if intersect_index >= len(self.events):
            return False

        event = self.events[intersect_index]

        return True if event[0] == start \
                       or end > event[0] and end < event[1] \
                       or start > event[0] and start < event[1] \
                       or start <= event[0] and end >= event[1] else False