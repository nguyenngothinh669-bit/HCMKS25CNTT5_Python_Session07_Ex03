RAW_DATA = " eMP-001; nguyen van a ;0987654321;sale | Emp-002; Tran Thi B; 0912-345-678 ; mkt | EMP-003 ; le van C ; 0988abc123 ; IT "


def parse_employee_data(raw_emp_string):

    fields = [field.strip() for field in raw_emp_string.split(';')]

    if len(fields) != 4:
        return None

    emp_id = fields[0].upper()
    name = fields[1].title()
    dept = fields[3].upper()

    phone_raw = fields[2].replace('-', '')
    if phone_raw.isdigit():
        phone = '******' + phone_raw[6:]
    else:
        phone = 'Invalid Format'

    return emp_id, name, phone, dept


def main():
    while True:
        print("===== HỆ THỐNG QUẢN LÝ NHÂN SỰ =====")
        print("1. Hiển thị chuỗi dữ liệu gốc")
        print("2. Chuẩn hóa dữ liệu và in báo cáo")
        print("3. Tìm kiếm nhân viên theo mã ID")
        print("4. Thoát chương trình")

        user_choice = input("Mời bạn chọn chức năng (1-4): ").strip()

        if user_choice == "1":
            print(f"\n[DỮ LIỆU GỐC]: {RAW_DATA}\n")

        elif user_choice == "2":
            employees_raw = RAW_DATA.split('|')

            print(f"\n{'ID':<10} | {'HỌ TÊN':<18} | {'SỐ ĐIỆN THOẠI':<15} | {'PHÒNG BAN':<10}")
            print("-" * 63)

            for emp_raw in employees_raw:
                employee_data = parse_employee_data(emp_raw)

                if employee_data:
                    emp_id, name, phone, dept = employee_data
                    print(f"{emp_id:<10} | {name:<18} | {phone:<15} | {dept:<10}")
            print()

        elif user_choice == "3":
            search_id = input("\nNhập mã nhân viên cần tìm: ").strip().upper()
            found = False

            employees_raw = RAW_DATA.split('|')
            for emp_raw in employees_raw:
                employee_data = parse_employee_data(emp_raw)

                if employee_data:
                    emp_id, name, phone, dept = employee_data

                    if emp_id == search_id:
                        print("\n=== THÔNG TIN NHÂN VIÊN TÌM THẤY ===")
                        print(f"Mã NV     : {emp_id}")
                        print(f"Họ và tên : {name}")
                        print(f"Số ĐT     : {phone}")
                        print(f"Phòng ban : {dept}\n")
                        found = True
                        break

            if not found:
                print("\n Không tìm thấy nhân viên\n")

        elif user_choice == "4":
            print("Thoát chương trình. Tạm biệt!")
            break

        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại số từ 1 đến 4!\n")


if __name__ == "__main__":
    main()