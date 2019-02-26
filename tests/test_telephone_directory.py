from String import telephone_name_lookup


def test_tel_directory():
    names = ['bevavy 2019830294','kim 94409294','smith 298234205','lewis 329049235','jim 392029446','peter 3425252525','john 23425255']

    (name_directory, phone_directory) = telephone_name_lookup.build_name_directory(names)
    results = telephone_name_lookup.lookup_number(238289, name_directory, phone_directory)

    assert {'bevavy': ['2019830294']} == results

    results = telephone_name_lookup.lookup_number(546, name_directory, phone_directory)

    assert {'kim': ['94409294'], 'jim': ['392029446']} == results
