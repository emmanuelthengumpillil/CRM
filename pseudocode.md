## START APP
↓
## Load CRM into memory ONCE
↓
## Loop:
    Ask user choice
    Execute logic on in-memory data
    Persist changes if needed
↓
## EXIT



## Input Layer (inpt.py)
    Ask questions
    Validate format only
    NO logic
    NO file access

## Logic Layer (crm.py)
    Add / remove / search / update
    Works ONLY on Python data structure
    Raises exceptions on invalid operations

## Storage Layer (storage.py)
    Load data once
    Save data when asked
    Knows NOTHING about validation rules

## App Controller (app.py)
    Main loop
    Calls input → logic → storage
    Handles exceptions
    Controls program flow