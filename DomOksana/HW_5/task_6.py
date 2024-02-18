st = input("введите текст: ")
s_del = input("введите знаки, которые надо убрать: ")
for sym in s_del:
    st = st.replace(sym, "")
print(f"строка без знаков {st}")
for sym in ["1","2","3","4","5","6","7","8","9","0"]:
    st = st.replace(sym, "")
print(f"строка без цифр {st}")
st = st.lower()
print(f"преобразуем строку в нижний регистр {st}")
st = st.replace(" ", "")
print(f"убираем пробелы {st}")
k = max(st, key = st.count)
print(f"чаще всего встречается буква {k}")