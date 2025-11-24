# Expense Splitter CLI

A minimal command-line application to record shared expenses among a group, compute net balances, and produce settlement instructions. Data is persisted to a local `data.json` file. This repository implements equal-split logic and provides an optional CSV export of settlement transactions.

Reference: course/project instructions PDF at `/mnt/data/BuildYourOwnProject.pdf`.



## Project title

**Expense Splitter CLI**



## Purpose / Objective

Provide a simple, reliable tool to:

* register participants,
* record bills paid by participants,
* split each bill equally among all registered participants,
* compute net balances and generate a minimal set of settlement instructions (who pays whom and how much),
* optionally export settlement instructions to `out.csv`.

This implementation is intended to meet the academic submission requirements for a simple group-expense tracker using only Python standard library features.



## Prerequisites

* Python 3.6 or later
* No external libraries required

Tested with Python 3.8+.



## Files

* `expense_splitter.py` — main script (place your provided code here).
* `data.json` — created/updated by the script; stores users and bills.
* `out.csv` — optional output generated after settlement calculation.
* `/mnt/data/BuildYourOwnProject.pdf` — project instructions (provided).



## Installation

1. Ensure Python 3 is installed:

   ```bash
   python3 --version
   ```
2. Place `expense_splitter.py` in a working directory.
3. Run the script from that directory:

   ```bash
   python3 expense_splitter.py
   ```



## Usage

When you run the script it shows a simple text menu:

```
1: user, 2: bill, 3: calc
>>
```

### Options

1. **Add user** (`1`)

   * Prompt: `name:`
   * Appends the name to the `"names"` list in `data.json`.

2. **Add bill** (`2`)

   * Prompts:

     * `amt:` (amount paid, numeric — decimal allowed)
     * `for:` (description of expense)
     * `payer:` (name of the user who paid)
   * The script divides the bill equally across all users currently recorded in `data.json`.
   * Creates a bill object with:

     ```json
     {
       "desc": "<description>",
       "total": <amount>,
       "who": "<payer>",
       "splits": { "<userA>": <share>, "<userB>": <share>, ... }
     }
     ```
   * The file `data.json` is overwritten with the updated `"names"` and `"data"` arrays after adding a bill.

3. **Calculate settlements** (`3`)

   * Computes net balances for each participant:

     * Each payer's balance increases by the `total` they paid.
     * Each participant's balance decreases by their share of each bill.
   * Balances are converted to integer cents to reduce floating-point rounding errors during settlement calculation.
   * The algorithm repeatedly matches a debtor (negative balance) with a creditor (positive balance) and creates settlement lines until no significant debts remain.
   * Outputs lines like:

     ```
     alice pays bob 25.0
     ```
   * After printing settlements, the script prompts:

     ```
     csv? y/n
     ```

     If `y`, it writes `out.csv` with header:

     ```
     from,to,amt
     ```



## Data format (example)

`data.json` structure:

```json
{
  "names": ["alice", "bob", "carol"],
  "data": [
    {
      "desc": "dinner",
      "total": 90.0,
      "who": "alice",
      "splits": { "alice": 30.0, "bob": 30.0, "carol": 30.0 }
    },
    {
      "desc": "snacks",
      "total": 45.0,
      "who": "bob",
      "splits": { "alice": 15.0, "bob": 15.0, "carol": 15.0 }
    }
  ]
}
```

`out.csv` example:

```
from,to,amt
alice,bob,25.0
```



## Example session

1. Start script.
2. Select `1` and add users: `alice`, `bob`, `carol`.
3. Select `2` and add a bill:

   * `amt:` 90
   * `for:` dinner
   * `payer:` alice
4. Select `2` and add another bill:

   * `amt:` 45
   * `for:` snacks
   * `payer:` bob
5. Select `3` to calculate:

   * Script prints settlement instructions.
   * Enter `y` to export `out.csv` if desired.



## Algorithm / Implementation notes

* Equal splitting only: each bill is divided by the current number of users.
* Balances computed in cents (`int(bal * 100)`) to minimize rounding errors; final outputs are converted back to decimal values.
* Settlement algorithm:

  * Repeatedly find any user with negative cents (debtor) and any user with positive cents (creditor).
  * Transfer the smaller of `abs(debtor)` and `creditor` between them and record the transaction.
  * Continue until no accounts have magnitude > 1 cent.
* Input validation is minimal. Non-numeric `amt` or nonexistent payer names may result in an error or the `bad input` message. Validate inputs before running for reliable results.
* `data.json` is overwritten on updates. Make backups if preserving history is important.



## Limitations and assumptions

* All splits are equal; there is no per-user custom share option.
* No deletion or editing of existing users or bills via the current interface.
* No timestamps are stored for bills.
* The script assumes payer names entered when adding a bill match exactly one of the names already stored.
* Concurrency is not handled: do not run multiple instances concurrently on the same `data.json`.



## Suggested improvements (for future versions)

* Support custom splits per bill.
* Add user/bill deletion and editing.
* Add timestamps and metadata for each bill.
* Improve input validation and user feedback.
* Add command-line arguments for non-interactive usage.
* Write unit tests to cover parsing, balance calculation, and settlement logic.
* Replace the JSON file with a lightweight database or add versioned backups.



## Testing checklist

1. Start with a fresh `data.json` (delete or rename the existing file).
2. Add multiple users.
3. Add several bills with different payers and amounts (integer and decimal values).
4. Run `3` and verify that:

   * Net balances match manual calculations.
   * Settlement lines reduce all balances to near zero.
5. Export CSV and verify rows follow `from,to,amt` format and amounts match printed values.





