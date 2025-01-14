num = []
for i in range(10):
    num.append(int(input(f"\nDigite o {i+1}° Número: ")))
print(f"""
+============================+>>>
| O Maior Número: {max(num)}
+============================+>>>
""")