from mnemonic import Mnemonic
from bip_utils import Bip39SeedGenerator, Bip32Slip10Secp256k1
from nostr.key import PrivateKey
import time

# Ruta de derivación para Nostr según NIP-06
NOSTR_DERIVATION_PATH = "m/44'/1237'/0'/0/0"

def generate_keys(pattern):
    npub_prefix = "npub1"
    attempts = 0
    start_time = time.time()

    while True:
        attempts += 1

        # Generar frase mnemónica y semilla
        mnemo = Mnemonic("english")
        mnemonic = mnemo.generate(strength=128)
        seed = Bip39SeedGenerator(mnemonic).Generate()

        # Derivar la clave privada
        bip32_ctx = Bip32Slip10Secp256k1.FromSeed(seed)
        derived_key = bip32_ctx.DerivePath(NOSTR_DERIVATION_PATH)
        private_key_bytes = derived_key.PrivateKey().Raw().ToBytes()

        # Generar clave privada y clave pública
        private_key = PrivateKey(private_key_bytes)
        npub = private_key.public_key.bech32()

        # Comprobar si el patrón coincide
        if npub[len(npub_prefix):].startswith(pattern):
            nsec = private_key.bech32()
            end_time = time.time()
            elapsed_time = end_time - start_time
            return mnemonic, nsec, npub, attempts, elapsed_time

if __name__ == "__main__":
    # Pedir el patrón al usuario
    pattern = input("Introduce el texto que debe tener después de 'npub1': ")

    # Generar claves
    mnemonic, nsec, npub, attempts, elapsed_time = generate_keys(pattern)

    # Mostrar resultados
    print(f"\nFrase mnemónica: {mnemonic}")
    print(f"Clave privada (nsec): {nsec}")
    print(f"Clave pública (npub): {npub}")
    print(f"Intentos: {attempts}")
    print(f"Tiempo total: {elapsed_time:.2f} segundos")
