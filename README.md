
# ☕ Welcome to the Python Coffee Vending Machine! ☕

Hello there, coffee lover! 👋

This little program brings the experience of a simple coffee vending machine right to your computer terminal. It's built using Python and follows procedural programming principles, meaning we've broken down the coffee-making process into a series of steps and functions.

Whether you're new to programming or just curious, we hope you enjoy interacting with it!

## What Can This Coffee Machine Do? 🧐

Our coffee machine can:

* **Serve Coffee:** Choose from our menu of espresso, latte, or cappuccino.
* **Check Resources:** It knows how much water, milk, and coffee it has left.
* **Process Coins:** You can "insert" virtual coins (quarters, dimes, nickels, pennies) to pay.
* **Calculate Change:** If you pay more than the cost, it will give you the correct change.
* **Generate Reports:** You can ask for a report to see the current resource levels and money earned.
* **Turn Off:** Politely say "off" when you're done.

## Getting Started: Running the Machine 🚀

It's easy to get your virtual coffee!

1.  **Make sure you have Python:** If you don't have Python installed, you'll need to install it first. You can find it at [python.org](https://www.python.org/downloads/).
2.  **Save the Code:** Copy the Python code you have and save it in a file. Let's call it `coffee_machine.py`.
3.  **Open a Terminal (or Command Prompt):**
    * On Windows, search for "cmd" or "PowerShell".
    * On macOS, search for "Terminal".
    * On Linux, you probably already know how to find your terminal! 😉
4.  **Navigate to the File:** In your terminal, use the `cd` command to go to the directory where you saved `coffee_machine.py`. For example, if it's in a folder called "MyPythonProjects" on your Desktop, you might type something like:
    ```bash
    cd Desktop/MyPythonProjects
    ```
5.  **Run the Program:** Type the following command and press Enter:
    ```bash
    python coffee_machine.py
    ```

And that's it! The coffee machine should start up.

## How to Use the Machine: Your Coffee Journey 🚶‍♀️➡️☕

Once the program is running, you'll see a friendly welcome message and a prompt:


----------------Welcome to the coffee machine program------------------
What would you like to make (espresso/latte/cappuccino):

Here's what you can type:

* **`espresso`**, **`latte`**, or **`cappuccino`**:
    1.  If you type the name of a coffee (like `espresso`), the machine will first check if it has enough ingredients.
    2.  If there aren't enough ingredients for your chosen drink, it will let you know (e.g., "There is not enough water").
    3.  If ingredients are sufficient, it will say:
        ```
        -------------------TIME TO PAY------------------
        Please enter some coins.
        ```
    4.  You'll then be asked to enter how many of each coin you're "inserting":
        * `How many quarters: ` (Enter a number, e.g., `4`)
        * `How many nickles: ` (Enter a number)
        * `How many pennies: ` (Enter a number)
        * `How many dimes: ` (Enter a number)
    5.  The machine will calculate the total amount you paid.
    6.  If you paid enough, it will tell you your change (if any) and "make" your coffee:
        ```
        Here is $X.XX in change
        -----------Transaction successful-----------
        Here is your Espresso ☕, enjoy!
        ```
    7.  If you didn't pay enough, it will say:
        ```
        Sorry, that is not enough, Money refunded!
        ```

* **`report`**:
    * If you type `report`, the machine will show you how much water, milk, coffee, and money it currently has:
        ```
        --------------COFFE MACHINE RESOURCES--------------
        water: 300ml
        milk: 200ml
        coffee: 100g
        Money: $0.0
        ```
        *(The values will change as you make coffee!)*

* **`off`**:
    * If you type `off`, the machine will shut down with a friendly:
        ```
        Goodbye 🙂
        ```

* **Anything Else**:
    * If you type something the machine doesn't understand, it will let you know:
        ```
        That is not in the Menu
        ```
        (It will print this message after a few blank lines).

## A Little Peek Inside the Code (Procedural Style) 🤓

This program is written using **procedural programming**. This means we've organized the code into a set of functions (procedures) where each function is responsible for a specific task.

You'll see functions like:

* `generate_report()`: Does what it says – creates the resource report!
* `check_sufficient_resources()`: Checks if we can make the drink.
* `process_coins()`: Handles getting coin input from you.
* `check_successful_transaction()`: Makes sure the payment is correct and gives change.
* `make_coffee()`: "Dispenses" your coffee and updates the resources.

The main part of the program is a `while` loop that keeps the machine "on" and waits for your commands. It then calls the appropriate functions based on your input.

We also have some data stored at the beginning:
* `MENU`: A dictionary that holds all the details about each coffee drink (ingredients and cost).
* `resources`: A dictionary that keeps track of the current levels of water, milk, and coffee.
* `money`: A variable to store how much money the machine has collected.

## Want to Tinker? Future Ideas! 💡

Since this is a beginner-friendly project, here are some ideas if you feel like expanding it:

* Add more types of coffee to the `MENU`.
* Implement a feature to refill resources.
* Allow different currency or coin types.
* Maybe even save the report to a file!


