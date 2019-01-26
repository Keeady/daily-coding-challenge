from Array import MyCalendar


def test_book_calendar():
    calendar = MyCalendar.MyCalendar()

    '''
    assert True == calendar.book(10, 20)
    assert calendar.events == [[10, 20]]

    assert False == calendar.book(15, 25)
    assert calendar.events == [[10, 20]]

    assert True == calendar.book(20, 30)
    assert calendar.events == [[10, 20], [20, 30]]

    assert True == calendar.book(8, 10)
    assert calendar.events == [[8,10], [10, 20], [20, 30]]

    assert False == calendar.book(8, 15)
    assert calendar.events == [[8, 10], [10, 20], [20, 30]]

    assert False == calendar.book(11, 15)
    assert calendar.events == [[8, 10], [10, 20], [20, 30]]

    assert False == calendar.book(10, 15)
    assert calendar.events == [[8, 10], [10, 20], [20, 30]]

    assert False == calendar.book(10, 30)
    assert calendar.events == [[8, 10], [10, 20], [20, 30]]

    assert False == calendar.book(11, 30)
    assert calendar.events == [[8, 10], [10, 20], [20, 30]]

    assert True == calendar.book(35, 45)
    assert calendar.events == [[8, 10], [10, 20], [20, 30], [35, 45]]

    assert False == calendar.book(18, 56)
    assert calendar.events == [[8, 10], [10, 20], [20, 30], [35, 45]]
    
    '''

    assert False == calendar.book(32, 50)
    assert calendar.events == [[8, 10], [10, 20], [20, 30], [35, 45]]


    '''

    events = [[47, 50], [33, 41], [39, 45], [33, 42], [25, 32], [26, 35], [19, 25], [3, 8], [8, 13]]

    for event in events:
        calendar.book(event[0], event[1])

    print(calendar.events)

    assert False == calendar.book(18, 27)
    '''

