from String import folder_path_to_tree


def test_folder_path_tree():
    folders = ['home/users/camaria', 'home/admin/june', 'temp/xhsuexs', '/var/log', '/var/lib/php']
    root = folder_path_to_tree.create_folder_path_tree(folders)

    assert root.val == '/'
    assert len(root.children) == 3
    assert root.children.get('home') is not None
    assert len(root.children.get('home').children) == 2
    assert root.children.get('temp') is not None
    assert len(root.children.get('temp').children) == 1
    assert root.children.get('var') is not None
    assert len(root.children.get('var').children) == 2

    folders = ['home/users/.camaria.txt', 'home/admin/june', 'temp/xhsuexs', '/var/log/.yxt.txt', '/var/lib/php']
    root = folder_path_to_tree.create_folder_path_tree(folders)
    assert root.val == '/'
    assert len(root.children) == 3
    assert root.children.get('home') is not None
    home = root.children.get('home')
    assert home.children.get('users') is not None
    users = home.children.get('users')
    assert users.children.get('.camaria.txt') is not None

    folders = ['home/users/../../june' ]
    root = folder_path_to_tree.create_folder_path_tree(folders)
    assert root.val == '/'
    assert len(root.children) == 2
    assert root.children.get('home') is not None
    home = root.children.get('home')
    assert home.children.get('june') is None
    assert home.children.get('users') is not None
    users = home.children.get('users')
    assert users.children.get('..') is None
    assert root.children.get('june') is not None


    folders = ['home/users/../june']
    root = folder_path_to_tree.create_folder_path_tree(folders)
    assert root.val == '/'
    assert len(root.children) == 1
    assert root.children.get('home') is not None
    home = root.children.get('home')
    assert home.children.get('june') is not None
    assert home.children.get('users') is not None
    users = home.children.get('users')
    assert users.children.get('..') is None
    assert root.children.get('june') is None

    folders = ['home/users/../../../../../../../june']
    root = folder_path_to_tree.create_folder_path_tree(folders)
    assert root.val == '/'
    assert len(root.children) == 2
    assert root.children.get('june') is not None

    folders = ['../june']
    root = folder_path_to_tree.create_folder_path_tree(folders)
    assert root.val == '/'
    assert len(root.children) == 1
    assert root.children.get('june') is not None

    folders = ['/../june']
    root = folder_path_to_tree.create_folder_path_tree(folders)
    assert root.val == '/'
    assert len(root.children) == 1
    assert root.children.get('june') is not None

    folders = ['home/users/../../../../../../../june', 'home/users/june']
    root = folder_path_to_tree.create_folder_path_tree(folders)
    assert root.val == '/'
    assert len(root.children) == 2
    assert root.children.get('june') is not None
    home = root.children.get('home')
    users = home.children.get('users')
    assert users.children.get('june') is not None