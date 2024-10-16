package com.thecoders.cartunnbackend.iam.application.internal.commandservices;

import java.util.Optional;

import org.springframework.stereotype.Service;

import com.thecoders.cartunnbackend.iam.application.internal.outboundservices.tokens.TokenService;
import com.thecoders.cartunnbackend.iam.domain.services.ValidateTokenCommandService;

@Service
public class ValidaTokenCommandServiceImpl implements ValidateTokenCommandService {
    private final TokenService tokenService;

    public ValidaTokenCommandServiceImpl(TokenService tokenService) {
        this.tokenService = tokenService;
    }

    @Override
    public Optional<Boolean> handle(String token) {
        return Optional.of(tokenService.validateToken(token));
    }
}
