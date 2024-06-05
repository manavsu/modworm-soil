<style lang="postcss">
  :global(html) {
    @apply bg-gray-950 text-white;
  }
  :global(html) {
    caret-color: white;
  }
</style>

<slot />
<div class="flex flex-row justify-between items-end w-full text-white fixed bottom-0 p-1">
  <h class="text-xs" >modworm &copy; 2024</h>
  <h class="text-sm p-1">soil v0.0.0</h>
</div>