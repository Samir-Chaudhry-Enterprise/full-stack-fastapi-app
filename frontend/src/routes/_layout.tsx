import { Box, Flex } from "@chakra-ui/react"
import { createFileRoute, Outlet, redirect } from "@tanstack/react-router"

import AppBackground from "@/components/Common/AppBackground"
import Navbar from "@/components/Common/Navbar"
import Sidebar from "@/components/Common/Sidebar"
import { isLoggedIn } from "@/hooks/useAuth"

export const Route = createFileRoute("/_layout")({
  component: Layout,
  beforeLoad: async () => {
    if (!isLoggedIn()) {
      throw redirect({
        to: "/login",
      })
    }
  },
})

function Layout() {
  return (
    <>
      <AppBackground />
      <Flex direction="column" h="100vh" position="relative" zIndex="1">
        <Box
          css={{
            animation: "reveal 0.6s ease-out",
            animationDelay: "0ms",
          }}
        >
          <Navbar />
        </Box>
        <Flex flex="1" overflow="hidden">
          <Box
            css={{
              animation: "reveal 0.6s ease-out",
              animationDelay: "100ms",
            }}
          >
            <Sidebar />
          </Box>
          <Flex
            flex="1"
            direction="column"
            p={4}
            overflowY="auto"
            css={{
              animation: "reveal 0.6s ease-out",
              animationDelay: "200ms",
            }}
          >
            <Outlet />
          </Flex>
        </Flex>
      </Flex>
    </>
  )
}

export default Layout
