from qiskit import QuantumRegister, QuantumCircuit, transpile
from qiskit_aer import Aer, AerSimulator

q = QuantumRegister(1)
hello_qubit = QuantumCircuit(q)

hello_qubit.id(q[0])

sim = Aer.get_backend('aer_simulator')

newcircuit = transpile(hello_qubit, sim)

result = sim.run(newcircuit).result()

print(result.get_statevector())