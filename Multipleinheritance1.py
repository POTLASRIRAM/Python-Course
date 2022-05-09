class Father:
    f_name="p"
class Mother:
    m_name="l"
class Child(Father,Mother):
    c_name="s"
    print("Father = ",Father.f_name)
    print("Mother = ",Mother.m_name)
    print("Child = ",c_name)
