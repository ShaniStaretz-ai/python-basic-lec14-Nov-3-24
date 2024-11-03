# python-basic-lec14-Nov-3-24

## subjects learned:

* functions-continue:
    * a function can receive parameters
        * sum(x:int,y:int): sum(3)-x=3, y has a default/sum(y=4)- x must have default
        * can give default to the parameters (don't always have to give), default values can be given to all parameter
          or to the last ones.
        * if a parameter doesn't have a default it must be sent on the function's calling
        * the default parameter is None and add init to []:
      ```
       if l1 is None:
          l1 = []
      ```
* a function can return feedback- 1 value or more
    * for metadata/ visualization added the type of the returned value:
  ```
  def half_num(num)->int: returned value from int type
  .....
  ```
    * if not returns anything, add ->None
    * if the function can return 2 types, add -> int|None - return int or return None

## extra subjects:
