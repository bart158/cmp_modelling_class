from qiskit import (ClassicalRegister, QuantumRegister, QuantumCircuit, transpile)

q = QuantumRegister(2, name = "qubits")
c = ClassicalRegister(2, name = "bits")

circuit = QuantumCircuit(q, c)

circuit.h(q[0])
circuit.cx(q[0], q[1])

circuit.measure(q, c)

from qiskit_aer import Aer

M_simulator = Aer.backends(name = 'qasm_simulator')[0]

job = M_simulator.run(transpile(circuit, M_simulator))

result = job.result()

print(result.get_counts())
'''
S_simulator = Aer.backends(name = 'statevector_simulator')[0]

job = S_simulator.run(transpile(circuit, S_simulator))

result = job.result()

print(result.get_statevector())

'''