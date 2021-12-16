from __future__ import annotations
from typing import List


class Packet:
    V = (0, 3)
    T = (3, 6)

    @classmethod
    def packetfactory(cls, packet: str) -> Packet:
        _type = int(packet[cls.T[0]:cls.T[1]], 2)
        if _type == 4:
            return Literal(packet)
        else:
            return Operator(packet)

    def __init__(self, packet: str) -> None:
        self.version = int(packet[self.V[0]:self.V[1]], 2)
        self._type = int(packet[self.T[0]:self.T[1]], 2)

        self.len = 6

    def getversionsum(self) -> int:
        return self.version

    def evaluate(self) -> int:
        raise Exception()

    def __repr__(self) -> str:
        return f'version = {self.version}, type = {self._type}'


class Literal(Packet):
    def __init__(self, packet: str) -> None:
        super().__init__(packet)
        groups_str = ''

        in_groups = packet[self.T[1]:]

        for i in range(0, len(in_groups), 5):
            stop = (in_groups[i] == '0')
            groups_str += in_groups[i + 1:i + 5]

            self.len += 5

            if stop:
                break

        self.value = int(groups_str, 2)

    def evaluate(self) -> int:
        return self.value

    def __repr__(self) -> str:
        return super().__repr__() + f', value = {self.value}'


class Operator(Packet):
    I = (Packet.T[1], Packet.T[1] + 1)

    L_0 = (I[1], I[1] + 15)
    L_1 = (I[1], I[1] + 11)

    def __init__(self, packet: str) -> None:
        super().__init__(packet)

        self.packets: List[Packet] = []

        self.indictor = int(packet[self.I[0]:self.I[1]], 2)
        self.len += 1
        if self.indictor == 0:
            self.len += 15

            total_len = int(packet[self.L_0[0]:self.L_0[1]], 2)
            c_len = 0
            while c_len < total_len:
                new_packet = Packet.packetfactory(packet[self.L_0[1] + c_len:])
                c_len += new_packet.len
                self.packets.append(new_packet)

            self.len += total_len
        else:
            self.len += 11

            no_packets = int(packet[self.L_1[0]:self.L_1[1]], 2)
            c_len = 0
            for _ in range(no_packets):
                new_packet = Packet.packetfactory(packet[self.L_1[1] + c_len:])
                c_len += new_packet.len
                self.packets.append(new_packet)

            self.len += c_len

    def getversionsum(self) -> int:
        return self.version + sum(x.getversionsum() for x in self.packets)

    def evaluate(self) -> int:
        result = 0

        if self._type == 0:
            result = sum(x.evaluate() for x in self.packets)
        elif self._type == 1:
            result = 1
            for x in self.packets:
                result *= x.evaluate()
        elif self._type == 2:
            result = min(x.evaluate() for x in self.packets)
        elif self._type == 3:
            result = max(x.evaluate() for x in self.packets)
        elif self._type == 5:
            if self.packets[0].evaluate() > self.packets[1].evaluate():
                result = 1
            else:
                result = 0
        elif self._type == 6:
            if self.packets[0].evaluate() < self.packets[1].evaluate():
                result = 1
            else:
                result = 0
        elif self._type == 7:
            if self.packets[0].evaluate() == self.packets[1].evaluate():
                result = 1
            else:
                result = 0

        return result

    def __repr__(self) -> str:
        return super().__repr__() + ', inner_packets = {{{}}}'.format(
            ' || '.join(x.__repr__() for x in self.packets))


def part1(packet: str):
    print(Packet.packetfactory(packet).getversionsum())


def part2(packet: str):
    print(Packet.packetfactory(packet).evaluate())


def main():
    f = open('inputs/day16.txt')

    bin_in = ''
    for c in f.readline().strip():
        bin_in += bin(int(c, 16))[2:].rjust(4, '0')

    part1(bin_in)
    part2(bin_in)


if __name__ == '__main__':
    main()
