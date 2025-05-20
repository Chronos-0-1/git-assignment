class Pizza:
    def __init__(self, size, toppings):
        self.size = size
        self.toppings = toppings

    def describe(self):
        print(f"\n[{self.size} 사이즈 피자]")
        print("현재 토핑:", ', '.join(self.toppings))

    def add_topping(self, topping):
        self.toppings.append(topping)
        print(f"'{topping}' 토핑이 추가되었습니다.")


# 사전 정의된 토핑 메뉴
available_toppings = ["치즈", "페퍼로니", "베이컨", "올리브", "양파", "버섯"]

# 피자 사이즈 입력
size = input("피자 사이즈를 선택하세요 (Small / Medium / Large): ")

# 토핑 안내 및 선택
print("\n🍕 선택 가능한 토핑 목록:")
print(", ".join(available_toppings))

topping_input = input("원하는 토핑을 쉼표로 구분해 입력하세요: ")
toppings = [t.strip() for t in topping_input.split(",") if t.strip() in available_toppings]

# 피자 객체 생성
order = Pizza(size, toppings)
order.describe()

# 추가 토핑 입력
add_more = input("\n토핑을 추가하시겠어요? (Y/N): ").strip().upper()

if add_more == "Y":
    new_topping = input("추가할 토핑을 하나 입력하세요: ").strip()
    if new_topping in available_toppings:
        order.add_topping(new_topping)
    else:
        print("선택할 수 없는 토핑입니다.")

order.describe()
