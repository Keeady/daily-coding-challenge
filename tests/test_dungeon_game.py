from Matrix import dungeon_game


def test_dungeon():
    '''
    assert 7 == dungeon_game.calc_min_knight_health([[-2,-3,3],[-5,-10,1],[10,30,-5]])

    assert 7 == dungeon_game.calc_min_knight_health([[-2,-3,3],[-5,-1,1],[1,3,-5]])

    assert 1 == dungeon_game.calc_min_knight_health([[0,0,0],[0,0,0],[0,0,0]])

    assert 5 == dungeon_game.calc_min_knight_health([[-2,-3,3],[-1,-1,1],[1,3,-5]])

    assert 1 == dungeon_game.calc_min_knight_health([[1,0,2],[3,1,4],[0,2,0]])

    assert 29 == dungeon_game.calc_min_knight_health([[-1, -18, -2], [-3, -1, -4], [-1, -2, -21]])

    assert 18 == dungeon_game.calc_min_knight_health([[-11, -1, -2], [-3, -1, -4], [-1, -2, -2]])

    assert 23 == dungeon_game.calc_min_knight_health([[-11, 0, 0], [0, 0, 0], [0, 0, -11]])
    '''

    assert 4 == dungeon_game.calc_min_knight_health([[-3, 5]])
