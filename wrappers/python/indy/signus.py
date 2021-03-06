from .libindy import do_call, create_cb

from ctypes import *

import logging

async def create_and_store_my_did(wallet_handle: int,
                                  did_json: str) -> (str, str, str):
    logger = logging.getLogger(__name__)
    logger.debug("create_and_store_my_did: >>> wallet_handle: %s, did_json: %s",
                 wallet_handle,
                 did_json)

    if not hasattr(create_and_store_my_did, "cb"):
        logger.debug("create_wallet: Creating callback")
        create_and_store_my_did.cb = create_cb(CFUNCTYPE(None, c_int32, c_int32, c_char_p, c_char_p, c_char_p))

    c_wallet_handle = c_int32(wallet_handle)
    c_did_json = c_char_p(did_json.encode('utf-8'))

    res = await do_call('indy_create_and_store_my_did',
                        create_and_store_my_did.cb,
                        c_wallet_handle,
                        c_did_json)

    logger.debug("create_and_store_my_did: <<< res: %s", res)
    return res

async def replace_keys(wallet_handle: int,
                       did: str,
                       identity_json: str) -> (str, str):
    logger = logging.getLogger(__name__)
    logger.debug("replace_keys: >>> wallet_handle: %s, did: %s, identity_json: %s",
                 wallet_handle,
                 did,
                 identity_json)

    if not hasattr(replace_keys, "cb"):
        logger.debug("replace_keys: Creating callback")
        replace_keys.cb = create_cb(CFUNCTYPE(None, c_int32, c_int32, c_char_p, c_char_p))

    c_wallet_handle = c_int32(wallet_handle)
    c_did = c_char_p(did.encode('utf-8'))
    c_identity_json = c_char_p(identity_json.encode('utf-8'))

    res = await do_call('indy_replace_keys',
                        replace_keys.cb,
                        c_wallet_handle,
                        c_did,
                        c_identity_json)

    logger.debug("replace_keys: <<< res: %s", res)
    return res


async def store_their_did(wallet_handle: int,
                          identity_json: str) -> None:
    logger = logging.getLogger(__name__)
    logger.debug("store_their_did: >>> wallet_handle: %s, identity_json: %s",
                 wallet_handle,
                 identity_json)

    if not hasattr(store_their_did, "cb"):
        logger.debug("store_their_did: Creating callback")
        store_their_did.cb = create_cb(CFUNCTYPE(None, c_int32, c_int32))

    c_wallet_handle = c_int32(wallet_handle)
    c_identity_json = c_char_p(identity_json.encode('utf-8'))

    res = await do_call('indy_store_their_did',
                        store_their_did.cb,
                        c_wallet_handle,
                        c_identity_json)

    logger.debug("store_their_did: <<< res: %s", res)
    return res


async def sign(wallet_handle: int,
               did: str,
               msg: str) -> str:
    logger = logging.getLogger(__name__)
    logger.debug("sign: >>> wallet_handle: %s, did: %s, msg: %s",
                 wallet_handle,
                 did,
                 msg)

    if not hasattr(sign, "cb"):
        logger.debug("sign: Creating callback")
        sign.cb = create_cb(CFUNCTYPE(None, c_int32, c_int32, c_char_p))

    c_wallet_handle = c_int32(wallet_handle)
    c_did = c_char_p(did.encode('utf-8'))
    c_msg = c_char_p(msg.encode('utf-8'))

    res = await do_call('indy_sign',
                        sign.cb,
                        c_wallet_handle,
                        c_did,
                        c_msg)

    logger.debug("sign: <<< res: %s", res)
    return res


async def verify_signature(wallet_handle: int,
                           pool_handle: int,
                           did: str,
                           signed_msg: str) -> bool:
    logger = logging.getLogger(__name__)
    logger.debug("verify_signature: >>> wallet_handle: %s, pool_handle: %s, did: %s, signed_msg: %s",
                 wallet_handle,
                 pool_handle,
                 did,
                 signed_msg)

    if not hasattr(verify_signature, "cb"):
        logger.debug("verify_signature: Creating callback")
        verify_signature.cb = create_cb(CFUNCTYPE(None, c_int32, c_int32, c_bool))

    c_wallet_handle = c_int32(wallet_handle)
    c_pool_handle = c_int32(pool_handle)
    c_did = c_char_p(did.encode('utf-8'))
    c_signed_msg = c_char_p(signed_msg.encode('utf-8'))

    res = await do_call('indy_verify_signature',
                        verify_signature.cb,
                        c_wallet_handle,
                        c_pool_handle,
                        c_did,
                        c_signed_msg)

    logger.debug("verify_signature: <<< res: %s", res)
    return res


async def encrypt(wallet_handle: int,
                  pool_handle: int,
                  my_did: str,
                  did: str,
                  msg: str) -> (str, str):
    logger = logging.getLogger(__name__)
    logger.debug("encrypt: >>> wallet_handle: %s, pool_handle: %s, my_did: %s, did: %s, msg: %s",
                 wallet_handle,
                 pool_handle,
                 my_did,
                 did,
                 msg)

    if not hasattr(encrypt, "cb"):
        logger.debug("encrypt: Creating callback")
        encrypt.cb = create_cb(CFUNCTYPE(None, c_int32, c_int32, c_char_p, c_char_p))

    c_wallet_handle = c_int32(wallet_handle)
    c_pool_handle = c_int32(pool_handle)
    c_my_did = c_char_p(my_did.encode('utf-8'))
    c_did = c_char_p(did.encode('utf-8'))
    c_msg = c_char_p(msg.encode('utf-8'))

    res = await do_call('indy_encrypt',
                        encrypt.cb,
                        c_wallet_handle,
                        c_pool_handle,
                        c_my_did,
                        c_did,
                        c_msg)

    logger.debug("encrypt: <<< res: %s", res)
    return res


async def decrypt(wallet_handle: int,
                  my_did: str,
                  did: str,
                  encrypted_msg: str,
                  nonce: str) -> str:
    logger = logging.getLogger(__name__)
    logger.debug("decrypt: >>> wallet_handle: %s, my_did: %s, did: %s, encrypted_msg: %s, nonce: %s",
                 wallet_handle,
                 my_did,
                 did,
                 encrypted_msg,
                 nonce)

    if not hasattr(decrypt, "cb"):
        logger.debug("decrypt: Creating callback")
        decrypt.cb = create_cb(CFUNCTYPE(None, c_int32, c_int32, c_char_p))

    c_wallet_handle = c_int32(wallet_handle)
    c_my_did = c_char_p(my_did.encode('utf-8'))
    c_did = c_char_p(did.encode('utf-8'))
    c_encrypted_msg = c_char_p(encrypted_msg.encode('utf-8'))
    c_nonce = c_char_p(nonce.encode('utf-8'))

    res = await do_call('indy_decrypt',
                        decrypt.cb,
                        c_wallet_handle,
                        c_my_did,
                        c_did,
                        c_encrypted_msg,
                        c_nonce)

    logger.debug("decrypt: <<< res: %s", res)
    return res
