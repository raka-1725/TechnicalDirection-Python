shopping_list = ["milk", "eggs", "bread"]
target_stock = ["milk", "eggs"]
walmart_stock = ["milk", "eggs"]
heb_stock = ["milk", "eggs", "bread"]


print(f"You need to buy {shopping_list} from the store.")

for item in shopping_list:
        print(item)


def winning_store(shopping_list, target_stock, walmart_stock, heb_stock):
        if shopping_list == target_stock:
                return "Target"
        elif shopping_list == walmart_stock:
                return "Walmart"
        elif shopping_list == heb_stock:
                return "HEB"
        else:
                return None

def ask_to_shop():
        answer = input("Do you want to go shopping? (Y/N)").strip().lower()
        return answer in {"yes" , "y"}

def ask_yn(prompt):
        answer = input(prompt).strip().lower()
        return answer in {"yes", "y"}

def get_store_stock(store_name): 
        store_name = store_name.strip().lower()
        if store_name in ("target", "t"): 
                return "Target", target_stock 
        elif store_name in ("walmart", "W"):
                return "Walmart", walmart_stock 
        elif store_name in ("HEB", "h"): 
                return "HEB", heb_stock 
        else:
                return None, None
        
def print_winning_store(): 
        if not ask_to_shop():
                print("ok, no shopping trip today.")
                return None
        
        while True:
                store_name = input("Which store do you want to go to? (Target/Walmart/HEB)").strip()
                store_label, stock = get_store_stock(store_name)
                if stock is None:
                        print(f"Sorry, '{store_name}' is not a valid store choice.")
                        continue
                
                print(f"{store_name} has the follwoing stock: {stock}")
                if ask_yn(f"Does {store_label} have everything on the shopping list? (Y/N) : "):
                        print(f"Thanks for shopping at {store_label}")
                        return store_label

                print("Ok, let's try a different store")


if __name__ == "__main__":
        print_winning_store()
