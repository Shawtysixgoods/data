### Описание структуры
Связанный список — это набор узлов (Node), где каждый узел хранит данные и ссылку (указатель) на следующий узел.

- Односвязный список (Singly Linked List): каждый узел имеет только ссылку на следующий узел.

- Двусвязный список (Doubly Linked List): узел имеет ссылки и на следующий, и на предыдущий узел.

Главное отличие от массива: элементы не хранятся подряд в памяти. Вместо этого каждый элемент знает, где лежит следующий.

### Как строится структура
- Односвязный: первый узел называется “головой” (head), а каждый узел ссылается на следующий.

- Двусвязный: помимо ссылки на следующий узел, хранится ссылка на предыдущий (next и prev).


### Чем полезен связанный список и где используется
- Быстрое добавление/удаление (при известном узле): Если у вас есть ссылка на нужный узел, вставка или удаление соседнего элемента происходит за O(1).

- Гибкость в размере: Вам не нужно заранее выделять смежный блок памяти, каждый узел может храниться в произвольном месте в памяти.

- Особые случаи: Связанные списки активно используются в реализациях разнообразных структур данных (например, хеш-таблицы могут хранить коллизии в виде цепочек, реализованных связным списком) и для некоторых видов очередей/деков.