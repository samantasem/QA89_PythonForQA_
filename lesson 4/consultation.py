#API

contact = {
    "id":12,
    "name":"Anna",
    "email":"anna@gm.com"
}
req_field = {
    "id",
    "name",
    "email"
}
for field in req_field:
    assert field in contact, f"В ответе отсутствует поле{field}"


    def print_list_reverse(lst):
        if lst is None or not isinstance(lst, list) or len(lst) == 0:
            print("Wrong list")
            return
        reversed_lst = lst[::-1]
        print(reversed_lst)


    print_list_reverse([1, 2, 3, 4, 5])
    print_list_reverse([])
    print()


    def is_valid_point(point):
        if point is None:
            return None
        if isinstance(point, tuple) and len(point) == 0:
            return None
        if not isinstance(point, tuple):  # or len(point) != 2:
            return False
        if len(point) != 2:
            return False
        x, y = point
        if not isinstance(x(int, float)) or not isinstance(y, (int, float)):
            return False
        return True