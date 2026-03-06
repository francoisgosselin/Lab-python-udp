#PARTIE2
from pathlib import Path
p = Path("data/message.txt") 
s = p.read_text(encoding="utf-8") 
print(type(s), len(s)) 
print(s)
b = p.read_bytes() 
print(type(b), len(b)) 
print(b[:20]) 

b2 = s.encode("utf-8") 
s2 = b.decode("utf-8") 
print(len(b2), type(b2)) 
print(type(s2))  

"""
La longueur d'une chaine de caractères est plus grande ou égale à sa longueur en octets. Les chaines de caractères Python sont encodées en utf8 et chaque caractère peut avoir une longueur d'un ou plusieurs octets.
"""

#PARTIE3 
"""
import socket

HOST = "127.0.0.1"
PORT = 12350

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"Serveur UDP en écoute sur {HOST}:{PORT}")

    while True:
        data, addr = s.recvfrom(1024)

        print(f"Reçu {len(data)} octets de {addr}")
        print("Message :", data.decode("utf-8", errors="replace"))

        s.sendto(b"Message recu", addr)*/

"""
        #PARTIE4
import socket
import hashlib
from pathlib import Path

HOST = "127.0.0.1"
PORT = 12346

#Ici c'est pour lire message
msg = Path("data/message.txt").read_text(encoding="utf-8").encode("utf-8")

h = hashlib.sha256(msg).hexdigest()

# Créer payload : message + séparateur + hash


payload = msg + b"\x00" + h.encode("ascii")

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(payload, (HOST, PORT))

    data, _ = s.recvfrom(1024)
    print("Réponse serveur :", data.decode("utf-8"))

"""
Il manque la partie avec le nonce. Typiquement, on génère un nonce aléatoire puis on crée un hash du message et du nonce:
h = hashlib.sha256(msg + nonce)
On envoie le hash + le message + le nonce au serveur pour qu'il puisse vérifier l'intégrité du message
Le nonce sert à empêcher une attaque de type replay (ou rejeu) où un message d'une requête précédente est intercepté et renvoyé ultérieurement par l'attaquant.
"""
