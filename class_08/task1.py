from qiskit import (ClassicalRegister, QuantumRegister, QuantumCircuit, transpile)
from qiskit_aer import Aer

q = QuantumRegister(3, name = "qubits")
c = ClassicalRegister(3, name = "bits")
circuit = QuantumCircuit(q, c)

circuit.h(q)
#oracle
circuit.x(q[0])
circuit.x(q[2])
circuit.ccz(q[0], q[1], q[2])
circuit.x(q[0])
circuit.x(q[2])

#diffuser
circuit.h(q)
circuit.x(q)
circuit.ccz(q[0], q[1], q[2])
circuit.x(q)
circuit.h(q)

#measure
circuit.measure(q, c)
print()
print(circuit)
M_simulator = Aer.backends(name = 'qasm_simulator')[0]

job = M_simulator.run(transpile(circuit, M_simulator))

result = job.result()

print(result.get_counts())
