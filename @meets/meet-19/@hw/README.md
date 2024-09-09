# Трансформация на данни

Имаме файл с название **schedule.csv**, който съдържа следната информация:
- ден от седмицата
- служител и неговата смяна

<table border="1">
  <thead>
    <tr>
      <th>den</th>
      <th>penodelnik</th>
      <th>vtornik</th>
      <th>sriada</th>
      <th>chetvurtuk</th>
      <th>petuk</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Teodora</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Galin</td>
      <td>1</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Mihail</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
  </tbody>
</table>


### Задача 1
Транформирайте данните така че резултата от този файл да бъде представен като речник, с водещ ключ служител и смените в които той трябва да работи - представени в текстов вид.

### Задача 2
Транформирайте данните така че резултата от този файл да бъде представен като речник, с водещ ключ ДЕН от седмицата, стойностите трябва да бъде списък от речници в които водещ е ключ сляна а стойностите са служителите, които трябва да работят в рамките на тази смяна.