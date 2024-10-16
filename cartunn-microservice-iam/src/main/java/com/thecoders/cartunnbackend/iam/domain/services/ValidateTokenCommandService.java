package com.thecoders.cartunnbackend.iam.domain.services;

import java.util.Optional;

public interface ValidateTokenCommandService {
    Optional<Boolean> handle(String token);
}
