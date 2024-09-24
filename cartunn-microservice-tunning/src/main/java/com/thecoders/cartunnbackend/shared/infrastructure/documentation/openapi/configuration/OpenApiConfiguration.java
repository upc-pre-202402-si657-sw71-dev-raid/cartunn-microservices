package com.thecoders.cartunnbackend.shared.infrastructure.documentation.openapi.configuration;

import io.swagger.v3.oas.models.Components;
import io.swagger.v3.oas.models.ExternalDocumentation;
import io.swagger.v3.oas.models.OpenAPI;
import io.swagger.v3.oas.models.info.Info;
import io.swagger.v3.oas.models.info.License;
import io.swagger.v3.oas.models.security.SecurityRequirement;
import io.swagger.v3.oas.models.security.SecurityScheme;
import io.swagger.v3.oas.models.servers.Server;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.util.List;
// http://localhost:8080/swagger-ui/index.html

@Configuration
public class OpenApiConfiguration {
    @Bean
    public OpenAPI cartunnOpenApi() {
        var openApi = new OpenAPI();
        openApi
                .info(new Info()
                        .title("Cartunn Backend API")
                        .description("Cartunn backend application REST API documentation.")
                        .version("v1.0.0")
                        .license(new License().name("Apache 2.0")
                                .url("https://www.apache.org/licenses/LICENSE-2.0.html")))
                .externalDocs(new ExternalDocumentation()
                        .description("Cartunn Backend Wiki Documentation")
                        .url("https://cartunn-backend.wiki.github.io/docs"));

        // Return OpenAPI configuration object*/
        return openApi;
    }
}
