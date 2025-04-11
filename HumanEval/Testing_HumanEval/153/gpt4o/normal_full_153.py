def Strongest_Extension(class_name, extensions):
    
    strong = extensions[0]
    my_val = len([x for x in extensions[0] if x.isalpha() and x.isupper()]) - len([x for x in extensions[0] if x.isalpha() and x.islower()])
    for s in extensions:
        val = len([x for x in s if x.isalpha() and x.isupper()]) - len([x for x in s if x.isalpha() and x.islower()])
        if val > my_val:
            strong = s
            my_val = val

    ans = class_name + "." + strong
    return ans




def test():

    assert Strongest_Extension("ExampleClass", ["txt", "DOC", "pdf"]) == "ExampleClass.DOC"
    assert Strongest_Extension("MyClass", ["jpg", "PNG", "gif", "GIF"]) == MyClass.PNG
    assert Strongest_Extension("TestClass", ["abc", "DEF", "ghi"]) == "TestClass.DEF"
    assert Strongest_Extension("Class", ["aaA", "BbB", "CcC", "DdD"]) == Class.BbB
    assert Strongest_Extension("Sample", ["xyz", "XYZ"]) == "Sample.XYZ"
