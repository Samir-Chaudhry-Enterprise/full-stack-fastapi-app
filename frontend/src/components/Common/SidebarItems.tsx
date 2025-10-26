import { Box, Flex, Icon, Text } from "@chakra-ui/react"
import { useQueryClient } from "@tanstack/react-query"
import { Link as RouterLink } from "@tanstack/react-router"
import { FiBriefcase, FiHome, FiSettings, FiUsers } from "react-icons/fi"
import type { IconType } from "react-icons/lib"

import type { UserPublic } from "@/client"

const items = [
  { icon: FiHome, title: "Dashboard", path: "/" },
  { icon: FiBriefcase, title: "Items", path: "/items" },
  { icon: FiSettings, title: "User Settings", path: "/settings" },
]

interface SidebarItemsProps {
  onClose?: () => void
}

interface Item {
  icon: IconType
  title: string
  path: string
}

const SidebarItems = ({ onClose }: SidebarItemsProps) => {
  const queryClient = useQueryClient()
  const currentUser = queryClient.getQueryData<UserPublic>(["currentUser"])

  const finalItems: Item[] = currentUser?.is_superuser
    ? [...items, { icon: FiUsers, title: "Admin", path: "/admin" }]
    : items

  const listItems = finalItems.map(({ icon, title, path }) => (
    <RouterLink key={title} to={path} onClick={onClose}>
      <Flex
        gap={4}
        px={4}
        py={2}
        position="relative"
        borderRadius="6px"
        transition="all 0.2s ease"
        _hover={{
          bg: { base: "gray.100", _dark: "whiteAlpha.100" },
          color: { base: "orange.600", _dark: "orange.400" },
          transform: "translateX(2px)",
          _before: {
            opacity: 1,
            width: "2px",
          },
        }}
        _before={{
          content: '""',
          position: "absolute",
          left: 0,
          top: "50%",
          transform: "translateY(-50%)",
          height: "60%",
          width: "0px",
          bg: { base: "orange.500", _dark: "orange.400" },
          borderRadius: "0 2px 2px 0",
          opacity: 0,
          transition: "all 0.2s ease",
        }}
        alignItems="center"
        fontSize="sm"
      >
        <Icon as={icon} alignSelf="center" />
        <Text ml={2}>{title}</Text>
      </Flex>
    </RouterLink>
  ))

  return (
    <>
      <Text
        fontSize="xs"
        px={4}
        py={2}
        fontWeight="600"
        textTransform="uppercase"
        letterSpacing="wider"
        color={{ base: "gray.600", _dark: "gray.400" }}
        fontFamily="mono"
      >
        Menu
      </Text>
      <Box>{listItems}</Box>
    </>
  )
}

export default SidebarItems
