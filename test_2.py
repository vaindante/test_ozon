from dataclasses import dataclass


@dataclass(eq=False)
class Product:
    name: str = ''
    price: float = 0

    def __eq__(self, other):
        if not isinstance(other, Product):
            raise ValueError(f'not supported class: {type, other}')

        return (self.price, self.name) == (other.price, other.name)


p1 = Product('test_1', 10)
p2 = Product('test_2', 10)
p3 = Product('test_1', 11)
p4 = Product('test_3', 11)
p5 = Product('test_1', 10)

print(p1 == p2)
print(p1 == p3)
print(p1 == p4)
print(p1 == p5)
