# db-hack
 
Ваня, Привет. Положи `injection.py` рядом с файлом `manage.py`

```python
python manage.py shell
import injection
```
для себя:
```python
injection.main()
```
для другого ученика:
```python
injection.main('Имя Фамилия')
```