from lib.check_todo import has_todo
def test_has_todo():
#test case 1 (checking for positive case)
    assert has_todo("This is a simple task #TODO") == True

def test_has_todo_for_empty_str():
#test case 2 (checking empty string)
    assert has_todo("") == False

def test_has_todo_for_mixcase_words():
#test case 3 (checking for mixcase words)
    assert has_todo("do the excercise #TOdo") == False

def test_has_todo_for_string_without_hashtag():
    #test case 4 (checking if string has hastag)
    assert has_todo("TODO laundry") == False

def test_has_todo_for_semicolon():
    #test case 5 (check if semicolons break the code)
    assert has_todo("#TODO: a list of shopping") == True

