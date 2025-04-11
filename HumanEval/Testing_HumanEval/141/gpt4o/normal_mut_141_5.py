def file_name_check(file_name):
    
    suf = ['txt', 'exe', 'dll']
    lst = file_name.split(sep='.')
    if len(lst) != 2:
        return 'No'
    if not lst[1] in suf:
        return 'No'
    if len(lst[0]) == 0:
        return 'No'
    if not lst[0][0].isalpha():
        return 'No'
    t = len([x for x in lst[0] if x.isdigit()])
    if t > 3:
        return 'No'
    return 'Yes'



def test():
        assert file_name_check("document.txt") == 'Yes'
    assert file_name_check("document.exe") == 'Yes'
    assert file_name_check("document.dll") == 'Yes'
    assert file_name_check("doc1ument.txt") == 'Yes'
    assert file_name_check("doc12ument.txt") == 'Yes'
    assert file_name_check("doc123ument.txt") == 'Yes'
    assert file_name_check("doc1234ument.txt") == 'No'
    assert file_name_check("doc123ument.pdf") == 'No'
    assert file_name_check("document") == 'No'
    assert file_name_check(".txt") == 'No'
    assert file_name_check("1document.txt") == 'No'
    assert file_name_check("document.txtexe") == 'No'
    assert file_name_check("docu.ment.txt") == 'No'
    assert file_name_check("docu1.ment.txt") == 'No'  # New test case to catch the flaw
