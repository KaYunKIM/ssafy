package com.cafe.config;
import java.util.Arrays;

import javax.sql.DataSource;

import org.apache.ibatis.session.SqlSessionFactory;
import org.mybatis.spring.SqlSessionFactoryBean;
import org.mybatis.spring.SqlSessionTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.boot.jdbc.DataSourceBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Primary;
import org.springframework.core.io.support.PathMatchingResourcePatternResolver;


import io.swagger.annotations.ApiKeyAuthDefinition;
import io.swagger.annotations.Authorization;
import io.swagger.annotations.AuthorizationScope;
import io.swagger.annotations.SecurityDefinition;
import io.swagger.annotations.SwaggerDefinition;
import springfox.documentation.builders.ApiInfoBuilder;
import springfox.documentation.builders.AuthorizationCodeGrantBuilder;
import springfox.documentation.builders.OAuthBuilder;
import springfox.documentation.builders.PathSelectors;
import springfox.documentation.builders.RequestHandlerSelectors;
import springfox.documentation.service.ApiInfo;
import springfox.documentation.service.ApiKey;
import springfox.documentation.service.GrantType;
import springfox.documentation.service.SecurityScheme;
import springfox.documentation.service.TokenRequestEndpoint;
import springfox.documentation.spi.DocumentationType;
import springfox.documentation.spring.web.plugins.Docket;
import springfox.documentation.swagger2.annotations.EnableSwagger2;


@Configuration
@EnableSwagger2
@EnableAutoConfiguration
public class SwaggerConfig {
        /*    @Bean
            public Docket swaggerSpringMvcPlugin() {

              return new Docket(DocumentationType.SWAGGER_2)          
                .select()                                      
                .apis(RequestHandlerSelectors.basePackage("com.cafe"))
                .build();
            }
	*/
	
	 
	@Bean
	public Docket api() {
	    return new Docket(DocumentationType.SWAGGER_2)
	            .select()
	            .apis(RequestHandlerSelectors.any())
	            .paths(PathSelectors.any())
	            .build()
	            .apiInfo(apiInfo())
	            .securitySchemes(Arrays.asList(apiKey()));
	}

	private ApiInfo apiInfo() {
	    return new ApiInfoBuilder()
	            .title("Cafe Sns REST API Document")
	            .description("this is swagger for cafe sns rest api")
	            .termsOfServiceUrl("localhost")
	            .version("1.0")
	            .build();
	}

	private ApiKey apiKey() {
	    return new ApiKey("jwt_token", "Authorization", "header");
	}
	
	/*
	 * 각 token를 사용해야하는 api 위에 주석을 단다.
	 *@ApiOperation(value = "", authorizations = { @Authorization(value="jwtToken") })
	 */
}
	
