
<script lang="ts">
	import { page } from '$app/stores';
</script>

<div class="flex flex-col justify-center bg-gray-950 min-h-screen text-white">
    <h1 class="text-7xl mx-auto z-10">{$page.status}</h1>
    {#if $page.error}
        <h2 class="text-4xl mt-2 mx-auto z-10">{$page.error.message}</h2>
    {/if}
</div>