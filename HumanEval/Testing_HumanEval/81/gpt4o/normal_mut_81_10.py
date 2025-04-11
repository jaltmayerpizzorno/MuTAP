def numerical_letter_grade(grades):
    

   
    letter_grade = []
    for gpa in grades:
        if gpa == 4.0:
            letter_grade.append("A+")
        elif gpa > 3.7:
            letter_grade.append("A")
        elif gpa > 3.3:
            letter_grade.append("A-")
        elif gpa > 3.0:
            letter_grade.append("B+")
        elif gpa > 2.7:
            letter_grade.append("B")
        elif gpa > 2.3:
            letter_grade.append("B-")
        elif gpa > 2.0:
            letter_grade.append("C+")
        elif gpa > 1.7:
            letter_grade.append("C")
        elif gpa > 1.3:
            letter_grade.append("C-")
        elif gpa > 1.0:
            letter_grade.append("D+")
        elif gpa > 0.7:
            letter_grade.append("D")
        elif gpa > 0.0:
            letter_grade.append("D-")
        else:
            letter_grade.append("E")
    return letter_grade



def test():
        assert numerical_letter_grade([4.0]) == ["A+"]
    assert numerical_letter_grade([3.8, 3.6]) == ["A", "A-"]
    assert numerical_letter_grade([2.9, 2.5]) == ['B', 'B-']
    assert numerical_letter_grade([1.9, 1.5]) == ['C', 'C-']
    assert numerical_letter_grade([0.9, 0.5, 0.0]) == ['D', 'D-', 'E']
    assert numerical_letter_grade([3.8, 3.6, 3.1, 2.8, 2.6, 2.1, 1.8, 1.6, 1.1, 0.8, 0.4, 0.0]) == ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E"]
