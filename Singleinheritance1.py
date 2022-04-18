class Parent:
    def student():
        student_name="s"
        student_rollno=23
class Child(Parent):
    def view():
        print(super().student())
c=Child()
c.view()
        