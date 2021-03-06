package org.hyperledger.indy.sdk.wallet;

import org.hyperledger.indy.sdk.ErrorCode;
import org.hyperledger.indy.sdk.ErrorCodeMatcher;
import org.hyperledger.indy.sdk.IndyIntegrationTest;
import static org.junit.Assert.assertNotNull;
import org.junit.Test;

import java.util.concurrent.ExecutionException;


public class CloseWalletTest extends IndyIntegrationTest {

	@Test
	public void testCloseWalletWorks() throws Exception {

		Wallet.createWallet("default", "closeWalletWorks", "default", null, null).get();

		Wallet wallet = Wallet.openWallet("closeWalletWorks", null, null).get();
		assertNotNull(wallet);

		wallet.closeWallet().get();
	}

	@Test
	public void testCloseWalletWorksForTwice() throws Exception {

		thrown.expect(ExecutionException.class);
		thrown.expectCause(new ErrorCodeMatcher(ErrorCode.WalletInvalidHandle));

		Wallet.createWallet("default", "closeWalletWorksForTwice", "default", null, null).get();

		Wallet wallet = Wallet.openWallet("closeWalletWorksForTwice", null, null).get();
		assertNotNull(wallet);

		wallet.closeWallet().get();
		wallet.closeWallet().get();
	}
}
