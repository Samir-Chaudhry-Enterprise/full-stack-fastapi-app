import { Flex, Image, Text, useBreakpointValue } from "@chakra-ui/react"
import { Link } from "@tanstack/react-router"

import Logo from "/assets/images/itemize-logo.png"
import UserMenu from "./UserMenu"

function Navbar() {
  const display = useBreakpointValue({ base: "none", md: "flex" })

  return (
    <Flex
      display={display}
      justify="space-between"
      position="sticky"
      color={{ base: "gray.800", _dark: "gray.100" }}
      align="center"
      bg={{ base: "white", _dark: "gray.900" }}
      borderBottom="1px solid"
      borderColor={{ base: "gray.200", _dark: "whiteAlpha.200" }}
      backdropFilter="blur(12px)"
      w="100%"
      top={0}
      px={6}
      py={3}
      zIndex={10}
    >
      <Link to="/">
        <Flex align="center" gap={3}>
          <Image src={Logo} alt="Logo" maxW="40px" />
          <Text
            fontFamily="heading"
            fontSize="xl"
            fontWeight="600"
            letterSpacing="tight"
            color={{ base: "gray.900", _dark: "gray.100" }}
          >
            Itemize
          </Text>
        </Flex>
      </Link>
      <Flex gap={2} alignItems="center">
        <UserMenu />
      </Flex>
    </Flex>
  )
}

export default Navbar
